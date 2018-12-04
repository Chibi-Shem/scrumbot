import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TimesheetboardComponent } from './timesheetboard.component';

describe('TimesheetboardComponent', () => {
  let component: TimesheetboardComponent;
  let fixture: ComponentFixture<TimesheetboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TimesheetboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TimesheetboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
