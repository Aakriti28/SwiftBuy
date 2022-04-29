import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {
  payment_id = 4;
  constructor( private _user : UserService ) { }

  ngOnInit(): void {
  }

  placeOrder() {
    this._user.placeOrder(this.payment_id).subscribe(
        response => {
          console.log("got payment id = ",  response);
        },
        error => {
          console.log("error in payment = ", error);
        }
      );
  }

}


