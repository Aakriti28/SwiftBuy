import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';

import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { HomePageComponent } from './home-page/home-page.component';
import { CatalogComponent } from './catalog/catalog.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
import { CatalogProductsComponent } from './catalog-products/catalog-products.component';
import { BuyHistoryComponent } from './buy-history/buy-history.component';
import { SellHistoryComponent } from './sell-history/sell-history.component';
import { AddProductComponent } from './add-product/add-product.component';
import { SellinfoComponent } from './sellinfo/sellinfo.component';
import { SellinfoUpdateProductComponent } from './sellinfo-update-product/sellinfo-update-product.component';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {MatIconModule} from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import {MatRadioModule} from '@angular/material/radio';
import {MatTooltipModule} from '@angular/material/tooltip';
import { RegisterComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { AuthService } from './auth.service';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomePageComponent,
    CatalogComponent,
    CatalogProductsComponent,
    BuyHistoryComponent,
    SellHistoryComponent,
    AddProductComponent,
    SellinfoComponent,
    SellinfoUpdateProductComponent,
    RegisterComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MDBBootstrapModule.forRoot(),
    BrowserAnimationsModule,
    MatCardModule,
    MatButtonModule,
    MatFormFieldModule,
    MatSelectModule,
    FormsModule,
    ReactiveFormsModule,
    MatIconModule,
    MatInputModule,
    MatRadioModule,
    MatTooltipModule,
    HttpClientModule,
    HttpClientXsrfModule
  ],
  providers: [AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
