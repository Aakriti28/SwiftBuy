import { Component, OnInit } from '@angular/core';
import { SellerService } from '../seller.service';

@Component({
  selector: 'app-sell-history',
  templateUrl: './sell-history.component.html',
  styleUrls: ['./sell-history.component.scss']
})
export class SellHistoryComponent implements OnInit {
  sell_history_list: any = [];
  constructor(private service: SellerService) { }

  ngOnInit(): void {
    this.getHistoryFromAPI()
  }

  getHistoryFromAPI(){
    this.service.getSellHistory().subscribe(
      response => {
        this.sell_history_list = response;
        this.sell_history_list = this.sell_history_list.results;
        console.log(this.sell_history_list)
      },
      error => {
        console.log("error in get_sell_history : ",error)
      }
    )
  }

}
