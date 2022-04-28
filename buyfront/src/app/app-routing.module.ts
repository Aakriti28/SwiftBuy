import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CatalogComponent } from './catalog/catalog.component';
import { NotificationComponent } from './notification/notification.component';

import { SignupComponent } from './signup/signup.component';
import {LoginComponent} from './login/login.component'

const routes: Routes = [
  { path: 'signup', component: SignupComponent },
  { path: 'notification', component: NotificationComponent},
  { path: 'catalog', component: CatalogComponent},
  { path: 'login', component: LoginComponent },
  // { path: 'cart', component: CartComponent},


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
