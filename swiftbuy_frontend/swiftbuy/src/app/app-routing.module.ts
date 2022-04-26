import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomePageComponent} from './home-page/home-page.component';


const routes: Routes = [
  {path:'homepage/:userid', component:HomePageComponent},
  // {path:'homepage/:userid', component:HomePageComponent},
];

// redirect '' to sign up page if user is logged in or to home page if not logged in
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
