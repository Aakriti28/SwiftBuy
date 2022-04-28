import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sellinfo-update-product',
  templateUrl: './sellinfo-update-product.component.html',
  styleUrls: ['./sellinfo-update-product.component.scss']
})
export class SellinfoUpdateProductComponent implements OnInit {
  product={
    name:"Nike Shoes",
    category:"First option",
    brand:"Nike",
    price:120,
    discount:30,
    quantity:10,
    image:"http://abcdefg",
    productDesc:"Comfy shoes for running",
    advertised:0

  }
  constructor() { }

  ngOnInit(): void {
  }

}
