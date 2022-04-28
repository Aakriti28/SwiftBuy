import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService } from '../_services/alert.service';
import { AuthenticationService } from '../_services/authentication.service';
import { UserService } from '../_services/user.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {

  registerForm: FormGroup;
  loading = false;
  submitted = false;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private authenticationService: AuthenticationService,
    private userService: UserService,
    private alertService: AlertService
  ) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      email: ['', Validators.required],
      name: ['', Validators.required],
      paymentId: ['', Validators.required]
  });

  }

  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;

    this.loading = true;
    // console.log('registerForm: ' + JSON.stringify(this.registerForm.value));
    this.userService.getPlaceOrder(this.registerForm.value)
        .pipe(first())
        .subscribe(
            data => {
                this.alertService.success('Payment method Registered', true);
                this.router.navigate(['/catalog']);
            },
            error => {
                this.alertService.error(error);
                this.loading = false;
            }
        );
  }

}


