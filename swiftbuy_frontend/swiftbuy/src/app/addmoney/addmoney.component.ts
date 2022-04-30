import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-addmoney',
  templateUrl: './addmoney.component.html',
  styleUrls: ['./addmoney.component.scss']
})
export class AddmoneyComponent implements OnInit {

  amount: number = 0;
  payment_method: number = 1;
  constructor(private service : UserService , private router: Router) { }

  ngOnInit(): void {
  }
  addMoney(){
    this.service.addMoney({"amount":this.amount, "payment_method":this.payment_method}).subscribe(
      response => {
        
        this.router.navigate(['/wallet'])
      },
      error => {
        console.log("error in add money : ",error)
      }
    )
  }
}
