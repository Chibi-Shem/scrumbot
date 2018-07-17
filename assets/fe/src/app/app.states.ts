import { ContentOnly } from './utils/layouts.utils'
import { CreateTeamComponent } from './components/forms/create-team/create-team.component'
import { JoinTeamComponent } from './components/prompts/join-team/join-team.component'

let CREATE_TEAM_STATE: Object[] = [
    {
        name: 'create-team',
        url: '/',
        views: ContentOnly(CreateTeamComponent),
    }
]

let JOIN_TEAM_STATE: Object[] = [
    {
        name: 'join-team',
        url: '/join',
        views: ContentOnly(JoinTeamComponent),
    }
]

export const APP_STATES = {
	otherwise: '/',
	states: [].concat(
		CREATE_TEAM_STATE,
        JOIN_TEAM_STATE
	)
}