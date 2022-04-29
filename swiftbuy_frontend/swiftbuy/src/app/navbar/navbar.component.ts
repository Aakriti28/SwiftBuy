import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(public _auth: AuthService, private router: Router) { }

  ngOnInit(): void {
  }
  logoutUser(){
    console.log("Logging out user");
    this._auth.logoutUser()
    .subscribe(
      (      res: any) =>{ 
        console.log(res);
        this._auth._isLoggedIn = false;
        this.router.navigate(['/login'])
      },
      err => {
        console.log(err);
        this._auth._isLoggedIn = true;
      }
    )
    console.log("logged out and ", this._auth._isLoggedIn );
  }
}
