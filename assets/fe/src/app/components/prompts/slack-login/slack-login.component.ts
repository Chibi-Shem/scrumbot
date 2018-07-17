import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-slack-login',
  templateUrl: './slack-login.component.html',
  styleUrls: ['./slack-login.component.css']
})
export class SlackLoginComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  login(){
      console.log('okie')
  }

}
