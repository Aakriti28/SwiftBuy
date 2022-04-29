import { Component, OnInit } from '@angular/core';
import { Registration_info } from '../registration_details';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  registerUserData:Registration_info = {
    name: '',
    email: '',
    role: '',
    address: '',
    referralToken: '',
    password: '',
    phone: 0,
    cpassword: '',
    shipaddress: ''
  };
  constructor(private _auth : AuthService, private router : Router) { }

  ngOnInit(): void {
  }

  registerUser(){
    console.log(this.registerUserData);
    this._auth.registerUser(this.registerUserData).subscribe(
      response => {
        console.log("registered new user. response = ",response);
        this.router.navigate(['/login']);
      },
      error => {
        console.log("eror in registering user = ",error);
        if (error.status == 432) alert("Password and Confirm password should match");
        else if (error.status == 487) alert("Invalid Referral token");
        else if (error.status == 415) alert("Invalid Email");
        else alert("Invalid Credentials");
      }
    );
  }
}
