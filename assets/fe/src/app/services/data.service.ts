import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { GET_LOGS,
        GET_ISSUES,
        GET_TIMESHEETS,
        GET_TEAM_MEMBERS,
        GET_TEAM_PROJECTS } from 'app/constants/endpoints';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(
      private http: HttpClient,
  ) { }

  users: {}
  projects: {}
  scrum_data: any

  fetchScrums(){
      return this.http.get(GET_LOGS())
  }

  fetchUsers(){
      return this.http.get(GET_TEAM_MEMBERS())
  }

  fetchProjects(){
      return this.http.get(GET_TEAM_PROJECTS())
  }

  fetchIssues(){
      return this.http.get(GET_ISSUES())
  }

  fetchTimesheets(){
      return this.http.get(GET_TIMESHEETS())
  }

  getScrums(){
      return this.scrum_data
  }

  getUsers(){
      return this.users
  }

  getProjects(){
      return this.projects
  }

  setScrums(scrum_data){
      this.scrum_data = scrum_data
  }

}
