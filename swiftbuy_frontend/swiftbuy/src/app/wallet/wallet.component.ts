import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
@Component({
  selector: 'app-wallet',
  templateUrl: './wallet.component.html',
  styleUrls: ['./wallet.component.scss']
})
export class WalletComponent implements OnInit {

  catalog_list: any = {};
  constructor(private service: UserService) { }
  // constructor(private service: CatalogService,public _auth: AuthService) { this._auth._isLoggedIn=true;console.log("logged in status is ", this._auth._isLoggedIn)}
  ngOnInit(): void {
    this.getCatalogFromAPI()
  }

  getCatalogFromAPI(){
    this.service.getWalletHistory().subscribe(
      response => {
        this.catalog_list = response;
        
        console.log(this.catalog_list)
      },
      error => {
        console.log("error in getcatalogFromAPI : ",error)
      }
    )
  }

  addMoney(){
    this.service.getWalletHistory().subscribe(
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
