# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='accounts.proto',
  package='private',
  syntax='proto3',
  serialized_options=b'Z\007.;proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0e\x61\x63\x63ounts.proto\x12\x07private\x1a\x1bgoogle/protobuf/empty.proto\"\'\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x18\n\x07\x41\x63\x63ount\x12\r\n\x05token\x18\x01 \x01(\t2\xba\x01\n\x0e\x41\x63\x63ountService\x12(\n\x06\x43reate\x12\r.private.User\x1a\r.private.User\"\x00\x12\x43\n\x1e\x41uthenticateByEmailAndPassword\x12\r.private.User\x1a\x10.private.Account\"\x00\x12\x39\n\x0e\x43hangePassword\x12\r.private.User\x1a\x16.google.protobuf.Empty\"\x00\x42\tZ\x07.;protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='private.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='private.User.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='private.User.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=95,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='private.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='private.Account.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:private.User)
  })
_sym_db.RegisterMessage(User)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'accounts_pb2'
  # @@protoc_insertion_point(class_scope:private.Account)
  })
_sym_db.RegisterMessage(Account)


DESCRIPTOR._options = None

_ACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='AccountService',
  full_name='private.AccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=124,
  serialized_end=310,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='private.AccountService.Create',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AuthenticateByEmailAndPassword',
    full_name='private.AccountService.AuthenticateByEmailAndPassword',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_ACCOUNT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChangePassword',
    full_name='private.AccountService.ChangePassword',
    index=2,
    containing_service=None,
    input_type=_USER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTSERVICE)

DESCRIPTOR.services_by_name['AccountService'] = _ACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
