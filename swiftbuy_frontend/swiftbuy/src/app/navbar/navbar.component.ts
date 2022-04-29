import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { CatalogService } from '../catalog.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  search_text:string = '';
  constructor(public _auth: AuthService, private router: Router, private cat_service: CatalogService) { }

  ngOnInit(): void {
  }
  logoutUser(){
    console.log("Logging out user");
    this._auth.logoutUser()
    .subscribe(
      (      res: any) =>{ 
        console.log(res);
        this._auth._isLoggedIn = false;
        this.router.navigate(['/login']);
        console.log("logged out ", this._auth._isLoggedIn);
      },
      err => {
        console.log(err);
        this._auth._isLoggedIn = true;
        console.log("error logging out ",this._auth._isLoggedIn);
      }
    )
  }

  onKeydown(event: { key: string; }) {
    if (event.key === "Enter") {
      console.log(event);
      console.log(this.search_text);
      
      this.cat_service.getSearchResults(this.search_text)
    .subscribe(
      (      res: any) =>{ 
        console.log(res);
        this.router.navigate(['/search_results']);
        console.log("search successful ", this._auth._isLoggedIn);
        this.cat_service.search_data = res.results;
        console.log(this.cat_service.search_data)
      },
      err => {
        console.log(err);
        console.log("error in search ",this._auth._isLoggedIn);
      }
    )
    }
  }
}
