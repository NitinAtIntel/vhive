// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package main

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// TempReaderClient is the client API for TempReader service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TempReaderClient interface {
	ReadTemp(ctx context.Context, in *TempReading, opts ...grpc.CallOption) (*Response, error)
}

type tempReaderClient struct {
	cc grpc.ClientConnInterface
}

func NewTempReaderClient(cc grpc.ClientConnInterface) TempReaderClient {
	return &tempReaderClient{cc}
}

func (c *tempReaderClient) ReadTemp(ctx context.Context, in *TempReading, opts ...grpc.CallOption) (*Response, error) {
	out := new(Response)
	err := c.cc.Invoke(ctx, "/TempReader/ReadTemp", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TempReaderServer is the server API for TempReader service.
// All implementations must embed UnimplementedTempReaderServer
// for forward compatibility
type TempReaderServer interface {
	ReadTemp(context.Context, *TempReading) (*Response, error)
	mustEmbedUnimplementedTempReaderServer()
}

// UnimplementedTempReaderServer must be embedded to have forward compatible implementations.
type UnimplementedTempReaderServer struct {
}

func (UnimplementedTempReaderServer) ReadTemp(context.Context, *TempReading) (*Response, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReadTemp not implemented")
}
func (UnimplementedTempReaderServer) mustEmbedUnimplementedTempReaderServer() {}

// UnsafeTempReaderServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TempReaderServer will
// result in compilation errors.
type UnsafeTempReaderServer interface {
	mustEmbedUnimplementedTempReaderServer()
}

func RegisterTempReaderServer(s grpc.ServiceRegistrar, srv TempReaderServer) {
	s.RegisterService(&TempReader_ServiceDesc, srv)
}

func _TempReader_ReadTemp_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(TempReading)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TempReaderServer).ReadTemp(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/TempReader/ReadTemp",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TempReaderServer).ReadTemp(ctx, req.(*TempReading))
	}
	return interceptor(ctx, in, info, handler)
}

// TempReader_ServiceDesc is the grpc.ServiceDesc for TempReader service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var TempReader_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "TempReader",
	HandlerType: (*TempReaderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ReadTemp",
			Handler:    _TempReader_ReadTemp_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "cmd/server/tempReader.proto",
}