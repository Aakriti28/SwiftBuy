import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {

  constructor(private _auth: AuthService) { }

  ngOnInit(): void {
  }
  logoutUser(){
    console.log("Logging out user");
    this._auth.logoutUser()
    .subscribe(
      (      res: any) => console.log(res),
      err => console.log(err)
    )
  }
}
