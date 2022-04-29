import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {
  payment_id = 4;
  constructor( private _user : UserService, private router : Router ) { }

  ngOnInit(): void {
  }

  placeOrder() {
    this._user.placeOrder(this.payment_id).subscribe(
        response => {
          console.log("got payment id = ",  response);
          this.router.navigate(['/home'])
        },
        error => {
          console.log("error in payment = ", error);
        }
      );
  }

}


