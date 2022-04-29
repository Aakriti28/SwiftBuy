import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  my_profile: any = {};
  constructor(private service: UserService) { }

  ngOnInit(): void {
    this.getMyProfileFromAPI()
  }
  
  getMyProfileFromAPI(){
    this.service.getProfile().subscribe(
      response => {
        this.my_profile = response;
        console.log(this.my_profile)
      },
      error => {
        console.log("error in get_my_profile : ",error)
      }
    )
  }

}
