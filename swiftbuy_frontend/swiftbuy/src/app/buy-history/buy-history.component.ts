import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-buy-history',
  templateUrl: './buy-history.component.html',
  styleUrls: ['./buy-history.component.scss']
})
export class BuyHistoryComponent implements OnInit {
  
  buy_history_list: any = [];
  constructor(private service: UserService) { }

  ngOnInit(): void {
    this.getHistoryFromAPI()
  }

  getHistoryFromAPI(){
    this.service.getBuyHistory().subscribe(
      response => {
        this.buy_history_list = response;
        this.buy_history_list = this.buy_history_list.results;
        console.log(this.buy_history_list)
       
      },
      error => {
        console.log("error in get_sell_history : ",error)
      }
    )
  }

}
