import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { Login_info } from '../login_details';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  loginUserData: Login_info = {
    email: '',
    password: ''
  };
  constructor(private _auth: AuthService, private router: Router) { }

  ngOnInit(): void {
  }

  loginUser() {
    // console.log(this.loginUserData);
    console.log(this.loginUserData);
    this._auth.loginUser(this.loginUserData)
    .subscribe(
      res => {
        console.log("success in login ",res);
        this._auth._isLoggedIn = true;
        this.router.navigate(['/catalog'])
      },
      // , 
      err => {
        console.log(err);
        this._auth._isLoggedIn = false;
      },

    )

  }
}
