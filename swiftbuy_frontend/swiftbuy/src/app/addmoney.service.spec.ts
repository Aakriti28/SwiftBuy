import { TestBed } from '@angular/core/testing';

import { AddmoneyService } from './addmoney.service';

describe('AddmoneyService', () => {
  let service: AddmoneyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AddmoneyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
