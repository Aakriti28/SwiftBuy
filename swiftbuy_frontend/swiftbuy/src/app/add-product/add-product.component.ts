import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import { Product_info } from '../product_details';
import { SellerService } from '../seller.service';
import { CatalogService } from '../catalog.service';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})


export class AddProductComponent implements OnInit{
  catalog_list: any = {}
  product: Product_info={
    name:"",
    category:"",
    brand:"",
    price:0,
    discount:0,
    quantity:0,
    image:"",
    productDesc:"",
    advertised:0

  };

  ngOnInit(): void {
    this.getCatalogFromAPI()
  }
  
  submitted = false;
  constructor(private service :SellerService, private cat_service: CatalogService) {}
  // constructor(public _auth: AuthService) { this._auth._isLoggedIn=true;console.log("logged in status is ", this._auth._isLoggedIn)}
  onSubmit() {
    this.submitted = true;
    console.log(this.product);
    
  }

  newProduct() {
    this.submitted = false;
    this.product = new Product_info('', '', '', 0,0,0,'','',0);
  }

  getCatalogFromAPI(){
    this.cat_service.getCatalog().subscribe(
      response => {
        this.catalog_list = response.results;
        console.log(this.catalog_list)
      },
      error => {
        console.log("error in getcatalogFromAPI : ",error)
      }
    )
  }

  addProduct(){
    this.service.addProduct(this.product).subscribe(
      response => {
        // console.log()
        console.log("added new product. response = ",response);
        // this.router.navigate(['/login']);
      },
      error => {
        console.log("eror in adding product = ",error);
      }
    );
  }
}
