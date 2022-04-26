import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SellinfoComponent } from './sellinfo.component';

describe('SellinfoComponent', () => {
  let component: SellinfoComponent;
  let fixture: ComponentFixture<SellinfoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SellinfoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SellinfoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
