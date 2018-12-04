import { ContentOnly } from 'app/utils/layouts.utils'
import { ScrumboardComponent } from 'app/components/containers/scrumboard/scrumboard.component'
import { IssueboardComponent } from 'app/components/containers/issueboard/issueboard.component'
import { TimesheetboardComponent } from './components/containers/timesheetboard/timesheetboard.component';
import { LoginComponent } from 'app/components/forms/login/login.component'
import { AuthenticationService } from 'app/services/authentication.service';

let HOME_STATE: Object[] = [
    {
        name: 'scrumboard',
        url: '/',
        views: ContentOnly(ScrumboardComponent),
    }
];

let ISSUES_STATE: Object[] = [
    {
        name: 'issuesboard',
        url: '/issues',
        views: ContentOnly(IssueboardComponent),
    }
];

let TIMESHEET_STATE: Object[] = [
    {
        name: 'timesheets',
        url: '/timesheets',
        views: ContentOnly(TimesheetboardComponent),
    }
];

let LOGIN_STATE: Object[] = [
    {
        name: 'login',
        url: '/login',
        views: ContentOnly(LoginComponent),
    }
];


let LOGOUT_STATE: Object[] = [
    {
        name: 'logout',
        url: '/logout',
        onEnter: function(trans, state){
            const auth = trans.injector().get(AuthenticationService);
            auth.rmToken();
            // Returns the router wihout using state service
            return trans.router.stateService.target('login');
        }
    }
];


export const APP_STATES = {
	states: [].concat(
        HOME_STATE,
        ISSUES_STATE,
        LOGIN_STATE,
        LOGOUT_STATE,
        TIMESHEET_STATE
	)
}