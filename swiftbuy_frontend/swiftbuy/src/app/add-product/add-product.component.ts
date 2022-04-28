import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import { Product_info } from '../product_details';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})


export class AddProductComponent {
  
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
  
  submitted = false;

  onSubmit() {
    this.submitted = true;
    console.log(this.product);
    
  }

  newProduct() {
    this.submitted = false;
    this.product = new Product_info('', '', '', 0,0,0,'','',0);
  }
}
