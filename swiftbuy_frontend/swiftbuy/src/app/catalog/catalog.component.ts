import { Component, OnInit } from '@angular/core';
import { CatalogService } from '../catalog.service';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {
  catalog_list: any = {};
  constructor(private service: CatalogService) { }
  // constructor(private service: CatalogService,public _auth: AuthService) { this._auth._isLoggedIn=true;console.log("logged in status is ", this._auth._isLoggedIn)}
  ngOnInit(): void {
    this.getCatalogFromAPI()
  }

  getCatalogFromAPI(){
    this.service.getCatalog().subscribe(
      response => {
        this.catalog_list = response;
        console.log(this.catalog_list)
      },
      error => {
        console.log("error in getcatalogFromAPI : ",error)
      }
    )
  }

}
