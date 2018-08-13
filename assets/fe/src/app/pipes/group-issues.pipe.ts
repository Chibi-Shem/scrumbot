import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'groupIssues'
})
export class GroupIssuesPipe implements PipeTransform {

  transform(issues: Object[], date: string): any {
      if(!issues){
          return null;
      }
      const grouped_issues = issues.reduce((previous, current)=> {
            var date_index = new Date(current['scrum_data'][date]).toLocaleDateString()
            if(!previous[date_index]) {
                previous[date_index] = [current];
            } else {
                previous[date_index].push(current);
            }
            return previous;
        }, {});
      return Object.keys(grouped_issues).map(date => ({ date, issues: grouped_issues[date] }));
  }

}
