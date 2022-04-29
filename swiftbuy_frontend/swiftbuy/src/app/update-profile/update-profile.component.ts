import { Component, OnInit } from '@angular/core';
import { Registration_info } from '../registration_details';
import { UserService } from '../user.service';
@Component({
  selector: 'app-update-profile',
  templateUrl: './update-profile.component.html',
  styleUrls: ['./update-profile.component.scss']
})

export class UpdateProfileComponent implements OnInit {
  my_profile: any = {};
  registerUserData:Registration_info = {
    name: '',
    email: '',
    role: '',
    address: '',
    referralToken: '',
    password: '',
    phone: 0,
    cpassword: '',
    shipaddress: ''
  };
  received_data = false;
  constructor(private service: UserService) { }

  ngOnInit(): void {
    this.getMyProfileFromAPI()
    // this.registerUserData = 
  }

  getMyProfileFromAPI(){
    this.service.getProfile().subscribe(
      response => {
        this.my_profile = response;
        this.my_profile = this.my_profile.results;
        this.received_data=true;
        this.registerUserData.address = this.my_profile.address;
        this.registerUserData.password = this.my_profile.password;
        this.registerUserData.cpassword = this.my_profile.password;
        if(this.my_profile.shipaddress){
          this.registerUserData.shipaddress = this.my_profile.shipaddress;
        }
        
        this.registerUserData.role = this.my_profile.role;
        this.registerUserData.referralToken = this.my_profile.referralToken;
        this.registerUserData.phone = this.my_profile.phone;
        this.registerUserData.email = this.my_profile.email;
        this.registerUserData.name = this.my_profile.name;
        this.received_data = true;
      },
      error => {
        console.log("error in get_my_profile : ",error)
      }
    )
  }

  updateUserInfo(){
    this.service.updateProfile(this.registerUserData).subscribe(
      response => {
        // console.log()
        console.log("registered new user. response = ",response);
        // this.router.navigate(['/login']);
      },
      error => {
        console.log("eror in registering user = ",error);
      }
    );
  }

}
