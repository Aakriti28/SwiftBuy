import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { ActivatedRoute } from '@angular/router';
import { first } from 'rxjs/operators';
import {Router} from '@angular/router';
import {Cart} from '../cart';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {

  product = [] as any;
  id: number;
  sub: any;

  cart: Cart = {
    product_id: 1,
    quantity: 1,

  }

  constructor(private route: ActivatedRoute, private userService: UserService, private router: Router) { 
    this.id=1;
  }

  ngOnInit(): void {
    this.sub = this.route.params.subscribe(params => {
      this.id = +params['product_id']; // (+) converts string 'id' to a number
      this.cart.product_id = this.id;
      console.log(this.id);
   });
    this.getProduct();
  }

  public buynow(){
    this.userService.addToCart(this.cart)
    .pipe(first())
    .subscribe(data =>
      {
        console.log("added new product, response = ",data);
        this.router.navigate(['/cart']);
      })
  }

  private getProduct() {
    this.userService.getProduct(this.id)
      .pipe(first())
      .subscribe(data => {
        this.product = data;
        console.log("hi! here is product data");
        console.log(data);
      });

      
  }

}
