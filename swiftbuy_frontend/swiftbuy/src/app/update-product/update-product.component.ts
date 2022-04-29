import { Component, OnInit } from '@angular/core';
import { SellerService } from '../seller.service';

@Component({
  selector: 'app-update-product',
  templateUrl: './update-product.component.html',
  styleUrls: ['./update-product.component.scss']
})
export class UpdateProductComponent implements OnInit {
  my_prods: any = {};
  constructor(private service: SellerService) { }

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts(){
    this.service.getSellerProduct().subscribe(
      response => {
        this.my_prods = response;
        console.log(this.my_prods)
      },
      error => {
        console.log("error in get_seller_products : ",error)
      }
    )
  }

}
