import { Component, OnInit } from '@angular/core';
import { INgxMyDpOptions } from 'ngx-mydatepicker';
import { DataService } from 'app/services/data.service';
import { faSearch, faAngleDown, faEllipsisV } from '@fortawesome/free-solid-svg-icons';
import { faCalendar } from '@fortawesome/free-regular-svg-icons';


@Component({
  selector: 'app-timesheetboard',
  templateUrl: './timesheetboard.component.html',
  styleUrls: ['./timesheetboard.component.scss']
})
export class TimesheetboardComponent implements OnInit {

  icons = {
    search: faSearch,
    calendar: faCalendar,
    ellipsis: faEllipsisV,
    angle_down: faAngleDown
  }

  today: Date = new Date();

  filter_to: Date = new Date();
  filter_from: Date = new Date(this.filter_to.getFullYear(),
                      this.filter_to.getMonth(),
                      this.filter_to.getDate()-6);

    from_model: any = {
      date: {
        year: this.filter_from.getFullYear(),
        month: this.filter_from.getMonth() + 1,
        day: this.filter_from.getDate()
      }
    };

    to_model: any = {
      date: {
        year: this.filter_to.getFullYear(),
        month: this.filter_to.getMonth() + 1,
        day: this.filter_to.getDate()
      }
    };

  
  from_yesterday = new Date(this.filter_from.getFullYear(),
                      this.filter_from.getMonth(),
                      this.filter_from.getDate()-1)

  to_tomorrow = new Date(this.filter_to.getFullYear(),
                      this.filter_to.getMonth(),
                      this.filter_to.getDate()+1)

  disabled_from = {
        year: this.from_yesterday.getFullYear(),
        month: this.from_yesterday.getMonth() + 1,
        day: this.from_yesterday.getDate()
      }

  disabled_to = {
        year: this.to_tomorrow.getFullYear(),
        month: this.to_tomorrow.getMonth() + 1,
        day: this.to_tomorrow.getDate()
      }

  fromOptions: INgxMyDpOptions = {
      dateFormat: 'mmm dd yyyy',
      disableSince: this.disabled_to
  };

  toOptions: INgxMyDpOptions = {
      dateFormat: 'mmm dd yyyy',
      disableUntil: this.disabled_from
  };

  constructor(
      private dataService: DataService,
  ) { }

  timesheets: any
  users: {}

  filtered_timesheets: any
  filter_user = ''

  ngOnInit() {
      this.fetchTimesheets()
      this.fetchUsers()
  }

  fetchUsers(){
      this.dataService.fetchUsers()
          .subscribe(
              data => {
                  this.users = data
              }
          );
  }

  fetchTimesheets(){
      this.dataService.fetchTimesheets()
          .subscribe(
              data => {
                this.timesheets = data
                this.filtered_timesheets = data
              }
          );
  }

  isWithinDate(timesheet_date, filter_from, filter_to){
    return (new Date(timesheet_date).setHours(0,0,0,0) >= filter_from.setHours(0,0,0,0) &&
            new Date(timesheet_date).setHours(0,0,0,0) <= filter_to.setHours(0,0,0,0))
  }

  setDateToFilter(to){
      this.filter_to = new Date(to.date.year,
                                  to.date.month-1,
                                  to.date.day);

      var tomorrow = new Date(this.filter_to.getFullYear(),
                      this.filter_to.getMonth(),
                      this.filter_to.getDate()+1)

      this.disabled_to.year = tomorrow.getFullYear()
      this.disabled_to.month = tomorrow.getMonth()+1
      this.disabled_to.day = tomorrow.getDate()
  }

  filteredExists(to_filter){
    let x = to_filter.filter(x => {
        return x.user_username.search(new RegExp(this.filter_user, 'i')) >= 0
      });
    return x.length;
  }
  
  returnToDisplayHumanizeTime(data){
    const humanize_time = data.timesheets[0].humanize_time.charAt(0).toUpperCase() + data.timesheets[0].humanize_time.slice(1);
    if (humanize_time == "Today" || humanize_time == "Tomorrow" || humanize_time == "Yesterday"){
       return humanize_time + " - ";
    }else{
      return "";
    }
    
  }

}
