import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'groupTimesheets'
})
export class GroupTimesheetsPipe implements PipeTransform {

  transform(timesheets: Object[], date: string): any {
      if(!timesheets){
          return null;
      }
      const grouped_timesheets = timesheets.reduce((previous, current)=> {
            var date_index = new Date(current[date]).toLocaleDateString()
            if(!previous[date_index]) {
                previous[date_index] = [current];
            } else {
                previous[date_index].push(current);
            }
            return previous;
        }, {});
      return Object.keys(grouped_timesheets).map(date => ({ date, timesheets: grouped_timesheets[date] }));
  }

}
