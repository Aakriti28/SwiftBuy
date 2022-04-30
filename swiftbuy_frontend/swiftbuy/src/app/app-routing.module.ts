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
import { SellHistoryComponent } from './sell-history/sell-history.component';
import { ProfileComponent } from './profile/profile.component';
import { WalletComponent } from './wallet/wallet.component';
import { UpdateProfileComponent } from './update-profile/update-profile.component';
import { AddmoneyComponent } from './addmoney/addmoney.component';
import { SearchResultComponent } from './search-result/search-result.component';
import { BuyHistoryComponent } from './buy-history/buy-history.component';
import { ProductComponent } from './product/product.component';

const routes: Routes = [
  {path:'home', component:HomePageComponent},
  {path:'', redirectTo:'/login',pathMatch:'full'},
  {path:'home/catalog/:category_name', component:CatalogProductsComponent},
  {path:'home/sellinfo/addproduct', component:AddProductComponent},
  {path:'home/sellinfo', component:SellinfoComponent},
  {path:'buy_history', component:BuyHistoryComponent},
  {path:'update', component:UpdateProductComponent},
  {path:'update/:product_id', component:SellinfoUpdateProductComponent},
  {path:'product/:product_id', component:ProductComponent},
  // {path:'home/catalog', component:CatalogComponent},
  {path:'login',component:LoginComponent},
  {path:'register',component:RegisterComponent},
  {path: 'catalog', component: CatalogComponent},
  {path: 'notifications', component: NotificationComponent},
  {path: 'cart', component: CartComponent},
  {path: 'sell_history', component: SellHistoryComponent},
  {path: 'profile', component: ProfileComponent},
  {path: 'order', component: OrderComponent},
  {path: 'wallet', component: WalletComponent},
  {path: 'profile/update', component:UpdateProfileComponent},
  {path: 'addmoney', component:AddmoneyComponent},
  {path: 'search_results', component:SearchResultComponent},
  {path: 'category/:category_id', component:CatalogProductsComponent}
];

// redirect '' to sign up page if user is logged in or to home page if not logged in
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
