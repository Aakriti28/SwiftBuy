import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Registration_info } from '../registration_details';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  my_profile: any = {
    name: 'hi'
  };
  registerUserData:Registration_info = {
    name: 'asasasas',
    email: '',
    role: '',
    address: '',
    referralToken: '',
    password: '',
    phone: 0,
    cpassword: '',
    shipaddress: ''
  };
  public receivedData = false;
  constructor(private service: UserService) { }

  ngOnInit(): void {
    this.getMyProfileFromAPI()
  }
  
  getMyProfileFromAPI(){
    this.service.getProfile().subscribe(
      response => {
        this.my_profile = response;
        this.my_profile = this.my_profile.results
        console.log(this.my_profile);
        this.receivedData = true;
      },
      error => {
        console.log("error in get_my_profile : ",error)
      }
    )
  }

  
}
