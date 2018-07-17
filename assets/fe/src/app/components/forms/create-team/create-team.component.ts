import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

import { ApiService } from '../../../services/api.service';

@Component({
  selector: 'app-create-team',
  templateUrl: './create-team.component.html',
  styleUrls: ['./create-team.component.css']
})
export class CreateTeamComponent implements OnInit {

  constructor(
      private apiService: ApiService
  ) { }

  ngOnInit() {
  }

  createTeam(createTeamForm: NgForm){
      this.apiService.create('accounts', createTeamForm.value);
  }
}
