import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomePageComponent} from './home-page/home-page.component';
import {CatalogComponent} from './catalog/catalog.component';
import {CatalogProductsComponent} from './catalog-products/catalog-products.component';
import {SellinfoComponent} from './sellinfo/sellinfo.component';
import {AddProductComponent} from './add-product/add-product.component';
import {SellinfoUpdateProductComponent} from './sellinfo-update-product/sellinfo-update-product.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { NotificationComponent } from './notification/notification.component';
import { CartComponent } from './cart/cart.component';
import { OrderComponent } from './order/order.component';
import { UpdateProductComponent } from './update-product/update-product.component';

const routes: Routes = [
  {path:'home', component:HomePageComponent},
  {path:'', redirectTo:'/login',pathMatch:'full'},
  {path:'home/catalog/:category_name', component:CatalogProductsComponent},
  {path:'home/sellinfo/addproduct', component:AddProductComponent},
  {path:'home/sellinfo', component:SellinfoComponent},
  {path:'update', component:UpdateProductComponent},
  {path:'update/:product_id', component:SellinfoUpdateProductComponent},
  // {path:'home/catalog', component:CatalogComponent},
  {path:'login',component:LoginComponent},
  {path:'register',component:RegisterComponent},
  {path: 'catalog', component: CatalogComponent},
  {path: 'notifications', component: NotificationComponent},
  {path: 'cart', component: CartComponent},
  {path: 'order', component: OrderComponent}
];

// redirect '' to sign up page if user is logged in or to home page if not logged in
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
