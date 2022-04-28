import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomePageComponent} from './home-page/home-page.component';
import {CatalogComponent} from './catalog/catalog.component';
import {CatalogProductsComponent} from './catalog-products/catalog-products.component';
import {SellinfoComponent} from './sellinfo/sellinfo.component';
import {AddProductComponent} from './add-product/add-product.component';
import {SellinfoUpdateProductComponent} from './sellinfo-update-product/sellinfo-update-product.component';



const routes: Routes = [
  {path:'home/:userid', component:HomePageComponent},
  // {path:'homepage/:userid', component:HomePageComponent},
  {path:'home/:userid/catalog/:category_name', component:CatalogProductsComponent},
  {path:'home/:userid/sellinfo/addproduct', component:AddProductComponent},
  {path:'home/:userid/sellinfo', component:SellinfoComponent},
  {path:'home/:userid/update/:product_id', component:SellinfoUpdateProductComponent},
  {path:'home/:userid/catalog', component:CatalogComponent},
];

// redirect '' to sign up page if user is logged in or to home page if not logged in
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
