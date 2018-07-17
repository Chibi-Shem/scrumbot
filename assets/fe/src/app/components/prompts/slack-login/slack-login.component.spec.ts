import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SlackLoginComponent } from './slack-login.component';

describe('SlackLoginComponent', () => {
  let component: SlackLoginComponent;
  let fixture: ComponentFixture<SlackLoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SlackLoginComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SlackLoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
