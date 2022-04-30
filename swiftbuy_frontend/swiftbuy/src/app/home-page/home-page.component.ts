import { Component, OnInit } from '@angular/core';
import { CatalogService } from '../catalog.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent implements OnInit {
  ads : any = [];
  constructor(private service: CatalogService) {}

  ngOnInit(): void {
    this.getAdsFromAPI()
  }

  getAdsFromAPI(){
    this.service.getAds()
      .subscribe(data => {
        this.ads = data;
        console.log(this.ads);
      });
  }
  // getAdvertismentsFromAPI(){
  //   if ( this.pid<1 ) {
  //     this.pid=1;
  //   }
//     this.service.getMatches(this.pid).subscribe(
//       response => {
//       // alert('Hi')
//       // console.log("Hi")
//       this.resp_list = response;
//       this.resp_list = this.resp_list.data;
//       if ( this.resp_list.length == 0 ) {
//         // this.pid=0;
//         this.pid=this.pid-1;
//         if(this.pid<1){
//           this.pid=1;
//         }
//       }
//       else {
//         this.match_list = this.resp_list;
//       }
//       // console.log(this.match_list[0])
//       // console.log("Response from API is : ", response)
//     },
//     error => {
//       // console.log("Oh no! Error is : ", error);
//       this.pid = 0;
//     })
// }

// import { Component, OnDestroy, OnInit } from '@angular/core';
// import { ActivatedRoute } from '@angular/router';
// import { MatchesService } from '../matches.service';

// @Component({
//   selector: 'app-matches',
//   templateUrl: './matches.component.html',
//   styleUrls: ['./matches.component.scss']
// })
// export class MatchesComponent implements OnInit, OnDestroy {
//   pid: number;
//   sub: any;
//   resp_list: any = [];
//   match_list: any = [];

//   constructor(private route: ActivatedRoute, private service : MatchesService) {
//     this.pid=1;
//     for (let i=0; i<10; i++) {
//       this.match_list[i] = { };
//     }
//   }

//   ngOnInit(): void {this.sub = this.route.params.subscribe(params => {

//     // console.log(params)
//     if('pid' in params){
//       this.pid = +params['pid']; // (+) converts string 'id' to a number
//     }
//     // console.log(this.pid)
//     });
//     this.getMatchesFromAPI();
//   }

//   ngOnDestroy() {
//     this.sub.unsubscribe();
//   }

//   getMatchesFromAPI(){
//     if ( this.pid<1 ) {
//       this.pid=1;
//     }
//     this.service.getMatches(this.pid).subscribe(
//       response => {
//       // alert('Hi')
//       // console.log("Hi")
//       this.resp_list = response;
//       this.resp_list = this.resp_list.data;
//       if ( this.resp_list.length == 0 ) {
//         // this.pid=0;
//         this.pid=this.pid-1;
//         if(this.pid<1){
//           this.pid=1;
//         }
//       }
//       else {
//         this.match_list = this.resp_list;
//       }
//       // console.log(this.match_list[0])
//       // console.log("Response from API is : ", response)
//     },
//     error => {
//       // console.log("Oh no! Error is : ", error);
//       this.pid = 0;
//     })
//   }

//   onNext(){
//     this.pid=this.pid+1;
//     this.getMatchesFromAPI();
//   }

//   onPrev(){
//     this.pid=this.pid-1;
//     if (this.pid<1) {
//       this.pid=1;
//     }
//     this.getMatchesFromAPI();
//   }

}