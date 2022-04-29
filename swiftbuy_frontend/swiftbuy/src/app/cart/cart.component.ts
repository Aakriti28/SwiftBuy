import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { UserService } from '../user.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  cart = [] as any


  constructor(
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.loadCart();
  }

  private loadCart() {
    this.userService.getCart()
      .pipe(first())
      .subscribe(data => this.cart = data);
      console.log(this.cart)
  }
}


