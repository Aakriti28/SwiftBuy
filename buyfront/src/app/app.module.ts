import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HttpClientModule } from '@angular/common/http';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NotificationComponent } from './notification/notification.component';
import { CatalogComponent } from './catalog/catalog.component';
import { ProductComponent } from './product/product.component';
import { CartComponent } from './cart/cart.component';
import { OrderComponent } from './order/order.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    NotificationComponent,
    CatalogComponent,
    ProductComponent,
    CartComponent,
    OrderComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
