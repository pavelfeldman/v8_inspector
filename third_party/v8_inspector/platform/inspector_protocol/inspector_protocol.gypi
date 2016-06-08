# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
{
  'variables': {
    'platform_inspector_protocol_files': [
      'Allocator.h',
      'Array.h',
      'BackendCallback.h',
      'Collections.h',
      'DispatcherBase.cpp',
      'DispatcherBase.h',
      'ErrorSupport.cpp',
      'ErrorSupport.h',
      'Maybe.h',
      'Object.cpp',
      'Object.h',
      'Parser.cpp',
      'Parser.h',
      'Platform.h',
      'FrontendChannel.h',
      'String16.h',
      'Values.cpp',
      'Values.h',
      'ValueConversions.cpp',
      'ValueConversions.h',
    ],
    'platform_inspector_protocol_wtf_files': [
      'CollectionsWTF.h',
      'PlatformWTF.h',
      'String16WTF.cpp',
      'String16WTF.h',
    ],
    'platform_inspector_protocol_files_stl': [
      'CollectionsSTL.h',
      'PlatformSTL.h',
      'String16STL.cpp',
      'String16STL.h',
    ],
    'platform_inspector_protocol_test_files': [
      'ParserTest.cpp',
    ]
  }
}
