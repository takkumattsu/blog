Objective-C カテゴリにプリミティブ型のプロパティを追加
==========================================================

カテゴリにプリミティブ型のプロパティを持たせる方法を調査したのでメモ

.. more::

基本的にはググるとたくさん出てくる方法の通り **objc_setAssociatedObject** と **objc_getAssociatedObject** を使う

例えばUIButtonにenum型のプロパティをカテゴリ拡張で持たせるとすると以下のようになる

MyButtonDefine.h

.. code-block:: objc
 
 #ifndef MyButton_Define_h
 #define MyButton_Define_h
 
 typedef NS_ENUM(NSInteger, MyButtonType)
 {
     HogeHogeType    = 1,
     PiyoPiyoType    = 2,
 };

 #endif


UIButton+TakkuMattsuCustom.h

.. code-block:: objc

 #import <UIKit/UIKit.h>
 #import "MyButtonDefine.h"

 @interface UIButton (TakkuMattsuCustom)
 @property (nonatomic) MyButtonType buttonType;
 @end


UIButton+TakkuMattsuCustom.m

.. code-block:: objc

 #import "UIButton+TakkuMattsuCustom.h"
 #import <objc/runtime.h>
 
 @implementation UIButton (TakkuMattsuCustom)
 
 - (void)setButtonType:(MyButtonType)buttonType
 {
     id value = [NSNumber numberWithInteger:buttonType];
     objc_setAssociatedObject(self, 
                              @selector(buttonType), 
                              value, 
                              OBJC_ASSOCIATION_RETAIN_NONATOMIC);
 }
 
 - (MyButtonType)buttonType
 {
     id value = objc_getAssociatedObject(self, @selector(buttonType));
     return [value integerValue];
 }
 
 @end

プリミティブ型をNSNumber型でラップしているだけ

.. author:: default
.. categories:: Objective-C
.. tags:: Objective-C
.. comments::
