import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SellinfoUpdateProductComponent } from './sellinfo-update-product.component';

describe('SellinfoUpdateProductComponent', () => {
  let component: SellinfoUpdateProductComponent;
  let fixture: ComponentFixture<SellinfoUpdateProductComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SellinfoUpdateProductComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SellinfoUpdateProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
