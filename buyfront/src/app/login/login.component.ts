import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService } from '../_services/alert.service';
import { AuthenticationService } from '../_services/authentication.service';
import { UserService } from '../_services/user.service';

// import { AlertService, AuthenticationService } from '@/_services';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  loading = false;
  submitted = false;

  // loginForm: FormGroup;
  // loading = false;
  // submitted = false;
  // returnUrl: string;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private authenticationService: AuthenticationService,
    private userService: UserService,
    private alertService: AlertService
    ) { }

  ngOnInit(): void {

    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
  });
}
    
  get f() { return this.loginForm.controls; }


  onSubmit() {
    this.submitted = true;
    this.loading = true;
    // console.log('registerForm: ' + JSON.stringify(this.loginForm.value));
    this.userService.login(this.loginForm.value)
        .pipe(first())
        .subscribe(
            data => {
                this.alertService.success('Login successful', true);
                console.log("Login Successful")
                this.router.navigate(['/catalog']);
            },
            error => {
                this.alertService.error(error);
                this.loading = false;
            }
        );
  }

}

