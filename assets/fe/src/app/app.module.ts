// ANGULAR MODULES
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { Pipe, PipeTransform } from '@angular/core';

// INSTALLED MODULES
import { DataTableModule } from 'angular-6-datatable';
import { UIRouterModule } from '@uirouter/angular';
import { NgxMyDatePickerModule } from 'ngx-mydatepicker';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CollapseModule } from 'ngx-bootstrap/collapse';
import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';
import { TimepickerModule } from 'ngx-bootstrap/timepicker';
import { SatPopoverModule } from '@ncstate/sat-popover';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

// IMPORTED FROM PROJECT
import { APP_STATES } from 'app/app.states';
import { AppComponent } from 'app/app.component';
import { ScrumboardComponent } from 'app/components/containers/scrumboard/scrumboard.component';
import { AvatarComponent } from 'app/components/avatar/avatar.component';
import { IssueboardComponent } from 'app/components/containers/issueboard/issueboard.component';
import { HeaderComponent } from 'app/components/header/header.component';
import { MarkerComponent } from 'app/components/marker/marker.component';
import { LoginComponent } from 'app/components/forms/login/login.component';
import { GroupbyDatePipe } from 'app/pipes/groupby-date.pipe';


@NgModule({
  declarations: [
    AppComponent,
    ScrumboardComponent,
    AvatarComponent,
    IssueboardComponent,
    HeaderComponent,
    MarkerComponent,
    GroupbyDatePipe,
    LoginComponent,
  ],
  imports: [
    NgbModule.forRoot(),
    BrowserModule,
    HttpClientModule,
    FontAwesomeModule,
    BrowserAnimationsModule,
    SatPopoverModule,
    CollapseModule.forRoot(),
    BsDatepickerModule.forRoot(),
    TimepickerModule.forRoot(),
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    }),
    UIRouterModule.forRoot(APP_STATES),
    FormsModule,
    DataTableModule,
    NgxMyDatePickerModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
