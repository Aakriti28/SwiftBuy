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
    referral_token: '',
    password: '',
    phone: 0
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
      }
    );
  }
}
