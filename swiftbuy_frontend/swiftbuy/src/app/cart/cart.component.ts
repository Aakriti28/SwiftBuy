import { Component, OnInit } from '@angular/core';
import { first } from 'rxjs/operators';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {
  cart = [] as any


  constructor(
    private userService: UserService, private router: Router ) { }

  ngOnInit(): void {
    this.loadCart();
  }

  redirect() {
    this.router.navigate(['/order']);
  }

  private loadCart() {
    this.userService.getCart()
      .pipe(first())
      .subscribe(data => this.cart = data);
      console.log(this.cart)
  }
}


