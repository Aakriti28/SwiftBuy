import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';

import { Product } from '../_models/product';
import { UserService } from '../_services/user.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {

  currentProduct: Product;

  constructor( private userService: UserService) { }

  ngOnInit(): void {
    
    this.userService.getProduct(1).subscribe(data => this.currentProduct = data)


  }

}

