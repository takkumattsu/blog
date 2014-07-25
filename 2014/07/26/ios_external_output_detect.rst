外部出力(AirPlayやHDMI)を検出する方法
=======================================

AVPlayerのexternalPlaybackActiveを利用せずに外部出力を検出する方法を調べることがあったのでメモしておきます。

.. more::

=======================
AVPlyaerを利用する方法
=======================

以下のようにAVPlayerのプロパティを利用すれば外部出力の検出できます。

`参考:AVPlayer Class Reference <https://developer.apple.com/library/ios/documentation/AVFoundation/Reference/AVPlayer_Class/Chapters/Reference.html#//apple_ref/occ/instp/AVPlayer/externalPlaybackActive>`_

登録
-----
.. code-block:: objc

 // externalPlaybackActiveのコールバック
 [_avPlayer addObserver:self
             forKeyPath:MVAvPlayerExternalPlaybackActive
                options:(NSKeyValueObservingOptionNew|NSKeyValueObservingOptionOld)
                context:nil];

KVO
----

.. code-block:: objc

 - (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
 {
     if ([keyPath isEqualToString:MVAvPlayerExternalPlaybackActive]) {
        // 検知したときの処理
     }
 }
     

ただ上記だとAVPlayerが再生していないと検知できません。
 
==========================
AVAudioSessionを利用する
==========================

`参考:Get name of AirPlay device using AVPlayer <http://stackoverflow.com/questions/13044894/get-name-of-airplay-device-using-avplayer>`_

上記はiOS7でdeprecatedなメソッドを利用しているので少し変更しました。

.. code-block:: objc

 - (BOOL)isExternalPlayback
 {
    __block BOOL isExternalOutput = NO;
    // 入出力を取得
    AVAudioSessionRouteDescription *audioRouteDesc = [[AVAudioSession sharedInstance] currentRoute];
    // 出力を取得
    NSArray *outputs = audioRouteDesc.outputs;
    [outputs enumerateObjectsUsingBlock:^(AVAudioSessionPortDescription *audioDesc, NSUInteger idx, BOOL *stop) {
        if([audioDesc.portType isEqualToString:AVAudioSessionPortAirPlay]){
            NSLog(@"AirPlay(๑˃̵ᴗ˂̵)و");
            *stop = YES;
            isExternalPlayback = YES;
        } else if ([audioDesc.portType isEqualToString:AVAudioSessionPortHDMI]){
            NSLog(@"HDMI(｡╹ω╹｡)");
            *stop = YES;
            isExternalOutput = YES;
        } else {
            // その他
        }
    }];
    
    return result;
 }

.. author:: default
.. categories:: iOS
.. tags:: iOS
.. comments::
