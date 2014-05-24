XcodeColors用のデバッグマクロ
==============================

Xcodeは他のIDEと違ってデバッグ時のログにフィルターがかけれない。(かけられるようにしてくれ)

そこで少しでも見やすくするために `XcodeColors <https://github.com/robbiehanson/XcodeColors>`_ を利用している。

その際のマクロをメモ

.. more::

XcodeColorsのインストールはcloneしてビルドすればOK

自分は以下のマクロを定義して使っている。

==============================
XXXX-Prefix.pch
==============================

.. code-block:: objc
 
 //
 // Prefix header for all source files of the 'XXX' target in the 'XXX' project
 //
  
 #import <Availability.h>
  
 #ifndef __IPHONE_3_0
 #warning "This project uses features only available in iOS SDK 3.0 and later."
 #endif
 
 #ifdef __OBJC__
 #import <UIKit/UIKit.h>
 #import <Foundation/Foundation.h>
 #endif
  
 #ifndef XCODE_COLORS_ESCAPE
 #define XCODE_COLORS_ESCAPE "\033["
 #endif
  
 #ifndef XCODE_COLORS_RESET_FG
 #define XCODE_COLORS_RESET_FG  XCODE_COLORS_ESCAPE "fg;" // Clear any foreground color
 #endif
  
 #ifndef XCODE_COLORS_RESET_BG
 #define XCODE_COLORS_RESET_BG  XCODE_COLORS_ESCAPE "bg;" // Clear any background color
 #endif
  
 #ifndef XCODE_COLORS_RESET
 #define XCODE_COLORS_RESET     XCODE_COLORS_ESCAPE ";"   // Clear any foreground or background color
 #endif
  
 // 通常
 #ifdef DEBUG
 #define TM_DEBUGLOG(...) NSLog(__VA_ARGS__)
 #else
 #define TM_DEBUGLOG(...)
 #endif
  
 // 青
 #ifdef DEBUG
 #define TM_B_DEBUGLOG(fmt,...) NSLog((@XCODE_COLORS_ESCAPE @"fg0,0,255;" @"== " @" %s(%d) " fmt @XCODE_COLORS_RESET), __FUNCTION__, __LINE__, ##__VA_ARGS__ );
 #else
 #define TM_B_DEBUGLOG(...)
 #endif
 
 // 緑
 #ifdef DEBUG
 #define TM_B_DEBUGLOG(fmt,...) NSLog((@XCODE_COLORS_ESCAPE @"fg30,160,90;" @"== " @" %s(%d) " fmt @XCODE_COLORS_RESET), __FUNCTION__, __LINE__, ##__VA_ARGS__ );
 #else
 #define TM_B_DEBUGLOG(...)
 #endif 
 
 // エラー用(赤)
 #ifdef DEBUG
 #define TM_ERROR_LOG(fmt,...)  NSLog((@XCODE_COLORS_ESCAPE @"fg255,0,0;" @"== " @" %s(%d) " fmt @XCODE_COLORS_RESET), __FUNCTION__, __LINE__, ##__VA_ARGS__ );
 #else
 #define TM_ERROR_LOG(fmt,...)
 #endif

例
----

.. code-block:: objc

 TM_DEBUGLOG(@"Normal");
 TM_B_DEBUGLOG(@"Blue");
 TM_G_DEBUGLOG(@"Green");
 TM_ERROR_LOG(@"Error");

出力
----

.. image:: ../../../_image/xcode_colors_sample.png


**追記**

`CocoaLumberjack <https://github.com/CocoaLumberjack/CocoaLumberjack>`_ 使うのがいい感じ?


.. author:: default
.. categories:: Xcode
.. tags:: Xcode
.. comments::
