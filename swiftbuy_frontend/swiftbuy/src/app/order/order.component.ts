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
          if (error.status == 415) alert('Insufficient quantity available in stock');
          else if (error.status == 411) alert("You don't have sufficient amount in wallet. Consider adding money to wallet");
          // else alert("You don't have sufficient amount in wallet. Consider adding money to wallet");
        }
      );
  }

}


